import graphene
from graphene_django import DjangoObjectType

from .models import ProductReview


class ProductReviewType(DjangoObjectType):
    class Meta:
        model = ProductReview
        fields = "__all__"


class CreateProductReview(graphene.Mutation):
    class Arguments:
        product_id = graphene.String(required=True)
        reviewer = graphene.String(required=True)
        details = graphene.String(required=True)

    product_review = graphene.Field(ProductReviewType)

    def mutate(self, info, product_id, reviewer, details):
        product_review = ProductReview(product_id=product_id, reviewer=reviewer, details=details)
        product_review.save()
        return CreateProductReview(product_review=product_review)


class Query(graphene.ObjectType):
    product_reviews = graphene.List(ProductReviewType)

    def resolve_product_reviews(self, info):
        """
        The resolve_posts function is a resolver. It’s responsible for retrieving the posts from the database and returning them to GraphQL.

        :param self: Refer to the current instance of a class
        :param info: Pass along the context of the query
        :return: All post objects from the database
        """
        return ProductReview.objects.all()


class Mutation(graphene.ObjectType):
    create_product_review = CreateProductReview.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
